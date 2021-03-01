# Composer Version Manager

[Composer 2](https://getcomposer.org/upgrade/UPGRADE-2.0.md) is here. It's time for a one stop shop for switching between major (and minor 
👶) composer versions. Erase "using the right composer version" from your workflow.

> But wait, what about `composer self-update --1` and `--2`?

Well I'm glad you've asked!

There are some added benefits this CLI and shell hook will bring to you:

1. Cached `composer.phar` for faster version toggling.
1. Per-directory smart composer environments. It's as simple as `cd my-project` and the right composer version will be used.

## Installation

Choose one of the options below to install cvm.

### Homebrew (MacOS)

```bash
brew update
brew install composer-version-manager/cvm/cvm
```

**Note:** Watch for symlink errors. If you already have an existing `Python3` installation you may be required to run the following command:

```bash
brew link --overwrite cvm
```

### Chocolatey (Windows)

*TODO*

### Download binary and update PATH

*TODO*

## Hook onto your shell

Hooking onto your shell enables cvm [Smart usage](#smart-usage) for per-directory automated composer verrsioning.

Find the instructions for your shell below. If your shell is not listed please feel free to [submit a feature request](https://github.com/composer-version-manager/cvm/issues/new) issue and we will try and make it happen.

### **BASH**

Add the following line to the end of your `~/.bashrc`

```bash
eval "$(cvm hook bash)"
```

### **ZSH**

Add the following line to the end of your `~/.zshrc`

```bash
eval "$(cvm hook zsh)"
```

## Smart usage

Create a `.cvm_config` in any directory specifying the composer version you would like to use. Navigating to that directory or any nested directory will automatically enable that composer version in your current workspace.

```bash
cd my-project
echo '2.0.11' > .cvm_config
```

This file can be committed to your source control.

## Global composer version

You can configure a global composer version. Which will be the default when no parent directory has a `.cvm_config`.

```
cvm list        # List available tags
cvm use 2.0.11  # Globally use a specific composer version
```

## Authors

### Morgan Wowk

Morgan is a Software Developer from the wintery lands of Canada 🇨🇦🍁. You can primarily find him on [LinkedIn](https://www.linkedin.com/in/morganwowk/), writing open source or building apps to help [tens of thousands of ecommerce stores](https://boldcommerce.com/).

### Bhavek Budhia

Likewise, Bhavek resides in the frosty country of Canada ☃️. An avid developer 👨‍💻 with fortified experience in Python that has helped us develop a clean and extendable codebase.
