from setuptools import setup, find_packages

setup(
    name="authz",
    version="0.1.0",
    description="Telegram bot license checker",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Creative Demon",
    author_email="your@email.com",
    url="https://github.com/yourusername/authz",
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot==20.0b0",
        "requests"
    ],
    python_requires=">=3.8",
)
