while True:
    try:
        if input() == "1234":
            print("OK")
            break
        print("FAIL")
    except EOFError:
        break