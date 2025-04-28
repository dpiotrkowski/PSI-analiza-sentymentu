import argparse
import subprocess

def run_script(script_name, *args):
    """Uruchom dany skrypt z argumentami"""
    command = ['python', script_name] + list(args)
    subprocess.run(command)

def main():
    parser = argparse.ArgumentParser(description="Command runner dla scraperow.")
    subparsers = parser.add_subparsers(dest='command')

    # Subparser dla reddit.py
    reddit_parser = subparsers.add_parser('reddit', help='Uruchom scraper Reddita')

    # Subparser dla x.py
    x_parser = subparsers.add_parser('x', help='Uruchom scraper X')

    # Subparser dla wykop.py
    wykop_parser = subparsers.add_parser('wykop', help='Uruchom scraper Wykop ')

    args = parser.parse_args()

    if args.command == 'reddit':
        subreddits = input("Podaj subreddity (rozdzielone przecinkiem): ")
        search_words = input("Podaj szukane słowa (rozdzielone przecinkiem): ")
        run_script('scrapers/reddit.py', subreddits, search_words)
    elif args.command == 'x':
        twitter_accounts = input("Podaj konta z X/Twitter (rozdzielone przecinkiem): ")
        run_script('scrapers/x.py', wykop_tags, x_accounts)
    elif args.command == 'wykop':
        wykop_tags = input("Podaj tagi z Wykopa (rozdzielone przecinkiem): ")
        run_script('scrapers/wykop.py', wykop_tags)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

