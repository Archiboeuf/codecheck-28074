def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

    def hello_world(string):
        return("Hello {}!".format(string))
    
    for i, v in enumerate(argv):
        print(hello_world(argv[i]))
        
#    for i, v in enumerate(argv):
#        print("argv[{0}]: {1}".format(i, v))
