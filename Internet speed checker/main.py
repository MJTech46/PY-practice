# internet speed checker
import speedtest

def check_speed():
    st = speedtest.Speedtest()
    print("Fetching best server based on ping...")
    st.get_best_server()
    
    print("Performing download test...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    
    print("Performing upload test...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    
    print("Performing ping test...")
    ping_result = st.results.ping

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping_result:.2f} ms")

if __name__ == "__main__":
    check_speed()
