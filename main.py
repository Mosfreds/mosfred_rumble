import vindinium

def main():
    # Create a vindinium client
    client = vindinium.Client(
        server='http://vindinium.org/',
        key='n0e4z0dj',
        mode='training',
        n_turns=3,
        open_browser=False
    )

    url = client.run(vindinium.bots.MinimaxBot())
    print('Replay in:', url)

if __name__ == '__main__':
    main()
