import requests

# The base URL for the proxyscrape API
API_BASE_URL = "https://api.proxyscrape.com/v2"

# Function to scrape proxies of a given type (HTTP, SOCKS4, or SOCKS5)
def scrape_proxies(proxy_type):
  # Send a request to the proxyscrape API to get the proxies
  response = requests.get(f"{API_BASE_URL}/?request=getproxies&protocol={proxy_type}&timeout=10000&country=all")
  if response.status_code != 200:
    print(f"Error getting {proxy_type} proxies:", response.text)
    return []
  
  # Split the response into lines and return the list of proxies
  return response.text.strip().split("\n")

# Scrape the HTTP, SOCKS4, and SOCKS5 proxies
http_proxies = scrape_proxies("http")
print("Scraped HTTP Proxies!")
socks4_proxies = scrape_proxies("socks4")
print("Scraped SOCKS4 Proxies!")
socks5_proxies = scrape_proxies("socks5")
print("Scraped SOCKS5 Proxies!") 

# Write the HTTP proxies to a file
with open("http_proxies.txt", "w") as f:
  for proxy in http_proxies:
    f.write(proxy + "\n")

# Write the SOCKS4 proxies to a file
with open("socks4_proxies.txt", "w") as f:
  for proxy in socks4_proxies:
    f.write(proxy + "\n")

# Write the SOCKS5 proxies to a file
with open("socks5_proxies.txt", "w") as f:
  for proxy in socks5_proxies:
    f.write(proxy + "\n")


# I added the print values to the code