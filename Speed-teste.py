pip install speedtest-cli

import speedtest

def run_speed_test():
    print("Iniciando teste de velocidade da internet...")
    st = speedtest.Speedtest()
    
    download_speed = st.download() / 1_000_000  # Convertendo para Mbps
    upload_speed = st.upload() / 1_000_000     # Convertendo para Mbps
    
    print(f"Velocidade de download: {download_speed:.2f} Mbps")
    print(f"Velocidade de upload: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    run_speed_test()
