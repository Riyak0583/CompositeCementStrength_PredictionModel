           # Function calling
import src.data_ingestion as data_ingestion
# Define Orchestron Model : Entry Point

def main():         # Function Defination
  # Step1 : Data Ingestion
  df = data_ingestion()
  print(df.head())

main()            # Function calling

