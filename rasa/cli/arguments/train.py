import argparse
from typing import Union

from rasa.cli.arguments.default_arguments import (
    add_config_param,
    add_stories_param,
    add_nlu_data_param,
    add_out_param,
    add_domain_param,
)
from rasa.constants import DEFAULT_CONFIG_PATH, DEFAULT_DATA_PATH


def set_train_arguments(parser: argparse.ArgumentParser):
    add_data_param(parser)
    add_config_param(parser)
    add_domain_param(parser)
    add_out_param(parser)

    add_augmentation_param(parser)
    add_debug_plots_param(parser)
    add_dump_stories_param(parser)

    add_model_name_param(parser)
    add_force_param(parser)
    add_compress_param(parser)


def set_train_core_arguments(parser: argparse.ArgumentParser):
    add_stories_param(parser)
    add_domain_param(parser)
    add_core_config_param(parser)
    add_out_param(parser)

    add_augmentation_param(parser)
    add_debug_plots_param(parser)
    add_dump_stories_param(parser)

    add_force_param(parser)

    add_model_name_param(parser)
    add_compress_param(parser)

    compare_arguments = parser.add_argument_group("Comparison Arguments")
    add_compare_params(compare_arguments)


def set_train_nlu_arguments(parser: argparse.ArgumentParser):
    add_config_param(parser)
    add_out_param(parser)

    add_nlu_data_param(parser)

    add_model_name_param(parser)
    add_compress_param(parser)


def add_force_param(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force a model training even if the data has not changed.",
    )


def add_data_param(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--data",
        default=[DEFAULT_DATA_PATH],
        nargs="+",
        help="Paths to the Core and NLU training files.",
    )


def add_core_config_param(parser: argparse.ArgumentParser):
    parser.add_argument(
        "-c",
        "--config",
        nargs="+",
        default=[DEFAULT_CONFIG_PATH],
        help="The policy and NLU pipeline configuration of your bot. "
        "If multiple configuration files are provided, multiple dialogue "
        "models are trained to compare policies.",
    )


def add_compare_params(
    parser: Union[argparse.ArgumentParser, argparse._ActionsContainer]
):
    parser.add_argument(
        "--percentages",
        nargs="*",
        type=int,
        default=[0, 5, 25, 50, 70, 90, 95],
        help="Range of exclusion percentages",
    )
    parser.add_argument(
        "--runs", type=int, default=3, help="Number of runs for experiments."
    )


def add_augmentation_param(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--augmentation",
        type=int,
        default=50,
        help="How much data augmentation to use during training.",
    )


def add_dump_stories_param(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--dump-stories",
        default=False,
        action="store_true",
        help="If enabled, save flattened stories to a file.",
    )


def add_debug_plots_param(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--debug-plots",
        default=False,
        action="store_true",
        help="If enabled, will create plots showing checkpoints "
        "and their connections between story blocks in a  "
        "file called `story_blocks_connections.html`.",
    )


def add_model_name_param(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--fixed-model-name",
        type=str,
        help="If set, the name of the model file/directory will be set to the given "
        "name.",
    )


def add_compress_param(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--store-uncompressed",
        action="store_true",
        help="If set the model is not compressed. Note: You need a compressed model "
        "file for running the Rasa Server, testing a model, etc.",
    )
