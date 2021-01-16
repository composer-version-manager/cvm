# Composer Version Manager

[Composer 2](https://getcomposer.org/upgrade/UPGRADE-2.0.md) is here. It's time for a one stop shop for switching between major (and minor 
👶) composer versions.

> But wait, what about `composer self-update --1` and `--2`?

Well I'm glad you've asked!

There are some added benefits this CLI will bring to you:

1. Cached `composer.phar` for faster version toggling.
1. Per-directory automated and configurable context switching.
1. Production and pipeline friendly installation via [Docker](https://hub.docker.com/).
1. It's as simple as `cvm 1` and `cvm 2`.

## Author

My name is Morgan Wowk and I am a Software Developer from the wintery lands of Canada 🇨🇦🍁. You can primarily find me on [LinkedIn](https://www.linkedin.com/in/morganwowk/), writing open source or building apps to help [tens of thousands of ecommerce stores](https://boldcommerce.com/).

## Usage

```
# All the commands below will install the missing
# version if it is not yet installed.

cvm 1               # Use the latest, stable composer 1
cvm 2               # Use the latest, stable composer 2
cvm 1.0.0-alpha7    # Use a specific release
```

