import os
import sys
import random
import string
import pathlib
import os.path as osp
import importlib.util

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_instance_from_file(file_path, class_name, *args, **kwargs):
    """
    Creates an instance of a class from a given file path.

    :param file_path: The file path where the class is defined.
    :param class_name: The name of the class to be instantiated.
    :param args: Positional arguments to be passed to the class constructor.
    :param kwargs: Keyword arguments to be passed to the class constructor.
    :return: An instance of the specified class, or None if creation fails.
    """
    # Normalize the file path
    file_path = os.path.abspath(file_path)

    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Extract module name and directory from the file path
    module_dir, module_file = os.path.split(file_path)
    module_name, _ = os.path.splitext(module_file)

    # Add module directory to sys.path
    if module_dir not in sys.path:
        sys.path.append(module_dir)

    # Load the module
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get the class and create an instance
    cls = getattr(module, class_name)
    instance = cls(*args, **kwargs)

    return instance

def get_function_from_file(file_path, function_name):
    """
    Gets a function from a given file path.

    :param file_path: The file path where the function is defined.
    :param function_name: The name of the function to be retrieved.
    :return: The function object, or None if retrieval fails.
    """
    try:
        # Normalize the file path
        file_path = os.path.abspath(file_path)

        # Check if the file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Extract module name and directory from the file path
        module_dir, module_file = os.path.split(file_path)
        module_name, _ = os.path.splitext(module_file)

        # Add module directory to sys.path
        if module_dir not in sys.path:
            sys.path.append(module_dir)

        # Load the module
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Get the function
        function = getattr(module, function_name)

        return function

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def run_function_from_file(file_path, function_name, *args, **kwargs):
    """
    Runs a function from a given file path.

    :param file_path: The file path where the function is defined.
    :param function_name: The name of the function to be executed.
    :param args: Positional arguments to be passed to the function.
    :param kwargs: Keyword arguments to be passed to the function.
    :return: The result of the function execution, or None if execution fails.
    """
    try:
        # Normalize the file path
        file_path = os.path.abspath(file_path)

        # Check if the file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Extract module name and directory from the file path
        module_dir, module_file = os.path.split(file_path)
        module_name, _ = os.path.splitext(module_file)

        # Add module directory to sys.path
        if module_dir not in sys.path:
            sys.path.append(module_dir)

        # Load the module
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Get the function and run it
        function = getattr(module, function_name)
        result = function(*args, **kwargs)

        return result

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def create_instance_from_file_source(source, class_name, *args, **kwargs):
    """
    Creates an instance of a class from a given source code.

    :param source: The source code where the class is defined.
    :param class_name: The name of the class to be instantiated.
    :param args: Positional arguments to be passed to the class constructor
    """
    # Create a temporary file to store the source code
    _home = pathlib.Path.home()
    dirname = osp.join(_home, ".appfl", "tmp")
    if not osp.exists(dirname):
        pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)
    file_path = osp.join(dirname, f"{id_generator()}.py")
    with open(file_path, "w") as file:
        file.write(source)

    # Create an instance from the temporary file
    instance = create_instance_from_file(file_path, class_name, *args, **kwargs)

    # Remove the temporary file
    os.remove(file_path)

    return instance

def get_function_from_file_source(source, function_name):
    """
    Gets a function from a given source code.

    :param source: The source code where the function is defined.
    :param function_name: The name of the function to be retrieved.
    :return: The function object, or None if retrieval fails.
    """
    # Create a temporary file to store the source code
    _home = pathlib.Path.home()
    dirname = osp.join(_home, ".appfl", "tmp")
    if not osp.exists(dirname):
        pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)
    file_path = osp.join(dirname, f"{id_generator()}.py")
    with open(file_path, "w") as file:
        file.write(source)

    # Get the function from the temporary file
    function = get_function_from_file(file_path, function_name)

    # Remove the temporary file
    os.remove(file_path)

    return function

def get_unique_filename(
    dirname: str,
    filename: str,
):
    """
    Create the directory (if needed) and get a unique filename by appending a number to the filename.
    :param dirname: The directory where the file is located.
    :param filename: The original filename.
    :return dirname, unique_filename: The directory and the unique filename.
    """
    if not osp.exists(dirname):
        pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)
    unique = 1
    unique_filename = filename
    filename_base, ext = osp.splitext(filename)
    while pathlib.Path(osp.join(dirname, unique_filename)).exists():
        unique_filename = f"{filename_base}_{unique}{ext}"
        unique += 1
    return dirname, unique_filename
