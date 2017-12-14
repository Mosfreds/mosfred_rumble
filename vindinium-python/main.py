import vindinium

def main():
    # Create a vindinium client
    client = vindinium.Client(
        server='http://vindinium.org/',
        key='n0e4z0dj',
        mode='training',
        n_turns=3,
        open_browser=True
    )

    url = client.run(vindinium.bots.MinerBot())
    print('Replay in:', url)

if __name__ == '__main__':
    main()
