try:
    file = open('python1.txt', 'r')
    content = file.read()
    a =b
    print(content)

except FileNotFoundError:
    print("The file does not exist")

except Exception as e:
    print("Error:", e)

finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print("File is closed")