import configparser

def read_config_file(filename):
    """
    Read a configuration file and return a ConfigParser object.
    """
    config = configparser.ConfigParser()
    config.read(filename)
    return config

def write_config_file(filename, config):
    """
    Write a ConfigParser object to a configuration file.
    """
    with open(filename, 'w') as configfile:
        config.write(configfile)

def merge_configs(default_config, override_config):
    """
    Merge two ConfigParser objects, overriding values from the default_config with values from the override_config.
    """
    merged_config = configparser.ConfigParser()
    merged_config.read_dict(default_config)
    for section in override_config.sections():
        if not merged_config.has_section(section):
            merged_config.add_section(section)
        for key, value in override_config.items(section):
            merged_config.set(section, key, value)
    return merged_config

if __name__ == "__main__":
    # Example usage:
    default_config = read_config_file('general.ini')
    override_config = read_config_file('custom.ini')
    merged_config = merge_configs(default_config, override_config)
    write_config_file('merged.ini', merged_config)


