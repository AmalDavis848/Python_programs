try:
    num=input("enter the input")
except KeyboardInterrupt as e:
    raise Exception(e)