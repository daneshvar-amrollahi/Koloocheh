from peer import serve, run
import sys

def main():
    print(sys.argv)
    if len(sys.argv) > 1:
        if (sys.argv[1] == "server"):
            serve()
        elif (sys.argv[1] == "client"):
            run()



if __name__ == "__main__":
    main()

