import click
import subprocess


@click.group()
def main(args=None):
    """Console script for chatbot"""
    pass


@main.group()
def log(args=None):
    """Log handling"""
    pass

@log.command()
def download(args=None):
    """Download log from server"""
    subprocess.call(["rsync", "-Pav", "root@undertheseanlp.com:/root/service/chatbot/logs/*", "logs"])
    print("Download log")


if __name__ == '__main__':
    main()
