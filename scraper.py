import csv
from datetime import datetime

def run_scraper():
    print("🚀 Starting Scraper...")
    data = [
        ["product_name", "source", "price", "timestamp"],
        ["Cloud Storage 1TB", "Amazon S3", "23.00", datetime.now().strftime("%Y-%m-%d %H:%M")],
        ["Cloud Storage 1TB", "Google Cloud", "20.00", datetime.now().strftime("%Y-%m-%d %H:%M")],
        ["Cloud Storage 1TB", "Azure Blob", "21.50", datetime.now().strftime("%Y-%m-%d %H:%M")],
        ["Compute Instance v2", "DigitalOcean", "40.00", datetime.now().strftime("%Y-%m-%d %H:%M")],
        ["Compute Instance v2", "Linode", "35.00", datetime.now().strftime("%Y-%m-%d %H:%M")],
        ["Compute Instance v2", "Vultr", "38.00", datetime.now().strftime("%Y-%m-%d %H:%M")],
        ["Managed Database", "AWS RDS", "120.00", datetime.now().strftime("%Y-%m-%d %H:%M")],
        ["Managed Database", "Google Cloud SQL", "115.00", datetime.now().strftime("%Y-%m-%d %H:%M")],
        ["Load Balancer", "DigitalOcean", "12.00", datetime.now().strftime("%Y-%m-%d %H:%M")],
        ["Load Balancer", "AWS ELB", "18.00", datetime.now().strftime("%Y-%m-%d %H:%M")]
    ]
    
    try:
        with open('market_data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        print("✅ SUCCESS: market_data.csv created!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_scraper()