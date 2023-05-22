# GitHub Organization Repo Cloner

This Python script allows you to clone all repositories from a specified GitHub organization. It has options for cloning to a specified path, compressing the cloned repositories into tar.gz files, and colorized output for improved readability. It also supports multi-threading for improved performance.

## Features

- Clones all repositories (public and private) from a specified GitHub organization
- Option to specify a clone path
- Option to compress cloned repositories into tar.gz files and delete the original directories
- Colorized output for start and finish of cloning
- Multi-threaded cloning for improved performance
- Progress bar based on the number of repositories cloned

## Installation

1. Clone this repository to your local machine.
2. Install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure `git` and `tar` are installed on your system and accessible from the command line.

## Usage

1. Open the `cloner.py` file in a text editor.
2. Replace `'your_github_token'` with your GitHub personal access token, `'organization_name'` with the name of the organization you want to clone, and `'clone_path'` (if desired) with the path where you want to clone the repositories. If you leave `'clone_path'` empty, the script will use the current working directory.
3. Set `COMPRESS` to `True` if you want to compress the repositories after cloning.
4. Save and close the file.
5. Run the script from the command line:

   ```bash
   python cloner.py
   ```

Enjoy your cloned repositories!

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
