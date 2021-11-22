from projectaile.utils.extractor_utils import resolve_csv
'''
    extract features and targets list from the csv
'''


def csv_extractor(config):
    train_config = config.data.dataset.train

    if 'valid' in config.data.dataset.keys():
        valid_config = config.data.dataset.valid
    else:
        valid_config = None

    train_df = None
    valid_df = None
    _pd_exists = False
    _col_exists = True
    separator = ','

    feature, feature_load_str = resolve_csv(
        train_config.features.interface_val, 'colname')
    target, target_load_str = resolve_csv(train_config.targets.interface_val,
                                          'colname')

    feature_col_idx = feature
    target_col_idx = target

    # Check if pandas exists
    try:
        import pandas as pd
        _pd_exists = True
    except ModuleNotFoundError:
        # Pandas not found, fallback to native loading...
        pass

    if _pd_exists:
        train_df = pd.read_csv(train_config.interface_path)
        if valid_config:
            valid_df = pd.read_csv(valid_config.interface_path)
    else:
        with open(train_config.interface_path, 'r') as f:
            # finding the column index of the feature and target columns
            train_df = f.readlines()
            # Assume first row is column names
            col_names = train_df[0]
            # Define the separator
            separator = ',' if '\t' not in col_names else '\t'

            entries = col_names.split(separator)

            # Check if first row is actually the column names by matching the feature_interface_name and target_interface_name
            if feature in entries or target in entries:
                feature_col_idx = col_names.index(feature)
                target_col_idx = col_names.index(target)
            else:
                _col_exists = False

            if _col_exists:
                train_df = train_df[1:]
#insert valid config check here
        with open(valid_config.interface_path, 'r') as f:
            valid_df = f.readlines()

            if _col_exists:
                valid_df = valid_df[1:]

    if _pd_exists:
        # Resolve File Names
        train_features = resolve_csv(train_df[feature_col_idx].tolist(), 'val',
                                     feature_load_str)
        train_targets = resolve_csv(train_df[target_col_idx].tolist(), 'val',
                                    target_load_str)
        valid_features = resolve_csv(valid_df[feature_col_idx].tolist(), 'val',
                                     feature_load_str)
        valid_targets = resolve_csv(valid_df[target_col_idx].tolist(), 'val',
                                    target_load_str)

    else:
        train_features = [
            resolve_csv(
                line.split(separator)[feature_col_idx], 'val',
                feature_load_str) for line in train_df
        ]
        train_targets = [
            resolve_csv(
                line.split(separator)[target_col_idx], 'val', target_load_str)
            for line in train_df
        ]
        valid_features = [
            resolve_csv(
                line.split(separator)[feature_col_idx], 'val',
                feature_load_str) for line in valid_df
        ]
        valid_targets = [
            resolve_csv(
                line.split(separator)[target_col_idx], 'val', target_load_str)
            for line in valid_df
        ]

    return train_features, valid_features, train_targets, valid_targets
