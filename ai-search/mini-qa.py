from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from datasets import load_dataset
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores.cassandra import Cassandra

ASTRA_DB_SECURE_BUNDLE_PATH = "./secure-connect-vector-database.zip"
ASTRA_DB_APPLICATION_TOKEN = "AstraCS:ZTgTuwAtcfhmoZiOMJsfTqtG:3dd86b0a38ad3551d84604029a434a049526827788c4595dae9ba5df0caf9f50"
ASTRA_DB_CLIENT_ID = "ZTgTuwAtcfhmoZiOMJsfTqtG"
ASTRA_DB_CLIENT_SECRET = "9mJgb2FESGCU9jdLR9B.W_LzU0qa+6nCak0w_AQsb+ZnXHjOW-radUtjzQA3ChAWCxYb_t.KDykw3kmvGCN2-x2wnpbU9ysIXvwiFiXRnJ,SxIPUadq-kIIUPw4QlbQ0"
ASTRA_DB_KEYSPACE = "search"
OPENAI_API_KEY = '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'

cloud_config = {
    'secure_connect_bundle': ASTRA_DB_SECURE_BUNDLE_PATH
}
auth_provider = PlainTextAuthProvider(
    ASTRA_DB_CLIENT_ID, ASTRA_DB_CLIENT_SECRET
)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
astraSession = cluster.connect()

llm = OpenAI(openai_api_key=OPENAI_API_KEY)
myEmbedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

myCassandraVStore = Cassandra(
    embedding=myEmbedding,
    session=astraSession,
    keyspace=ASTRA_DB_KEYSPACE,
    table_name="qa_mini_demo"
)

print("Loading data from huggingface...")
myDataset = load_dataset("Biddls/Onion_News", split="train")
headlines = myDataset["text"][:50]

print("\nGenerating embeddings and storing in AstraDB..")

print("Inserted %i headlines.\n" % len(headlines))

vectorIndex = VectorStoreIndexWrapper(vectorstore=myCassandraVStore)

first_question = True

while True:
    if first_question:
        query_text = input("\nEnter your question (or type 'quit' to exit): ")
        first_question = False
    else:
        query_text = input(
            "\nWhat's your next question (or type 'quit' to exit): ")

    if query_text.lower() == 'quit':
        break

    print("QUESTION: \"%s\"" % query_text)
    answer = vectorIndex.query(query_text, llm=llm).strip()
    print("ANSWER: \"%s\"" % answer)

    for doc, score in myCassandraVStore.similarity_search_with_score(query_text, k=4):
        print(" %0.4f \"%s\"" % (score, doc.page_content[:60]))
