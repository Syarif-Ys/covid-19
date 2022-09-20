import covid19_indonesia

if __name__ == "__main__":
    print("Aplikasi Tracking Covid-19 di Indonesia")
    result = covid19_indonesia.ekstraksi_data()
    covid19_indonesia.tampilkandata(result)