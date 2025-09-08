import time

def spam_text(text="SEND HIT SS TO BAYYMAX - ABOBE 500 OR BIZZ HITS", count=1000, delay=0.1):
    for i in range(count):
        print(f"{text}")
        time.sleep(delay)

if __name__ == "__main__":
    spam_text("SEND HIT SS TO BAYYMAX - ABOBE 500 OR BIZZ HITS", count=10000, delay=0.1) 
