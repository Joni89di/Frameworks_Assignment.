import pandas as pd

def main():
    try:
        df = pd.read_csv('metadata.csv', low_memory=False)
        print(f"Dataset shape: {df.shape}")
        print("Columns and types:")
        print(df.dtypes)
        print("\nMissing values:")
        print(df.isnull().sum())
    except FileNotFoundError:
        print("Please place 'metadata.csv' in the project directory.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
