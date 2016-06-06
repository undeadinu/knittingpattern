from knittingpattern.rendering.Instruction import Instruction
from pytest import fixture
from knittingpattern.Instruction import InstructionInRow
from unittest.mock import MagicMock
import os


HERE = os.path.dirname(__file__)
IMAGES_FOLDER = os.path.join(HERE, "test_images")
KNIT_FILE = os.path.join(IMAGES_FOLDER, "knit.svg")
PURL_FILE = os.path.join(IMAGES_FOLDER, "purl.svg")


@fixture
def instruction1():
    return Instruction({"type": "knit"})


@fixture
def knit():
    knit = Instruction({"type": "knit"})
    knit.load_image.relative_folder(__name__, "test_images")
    return knit


@fixture
def purl():
    purl = Instruction({"type": "purl"})
    purl.load_image.relative_folder(__name__, "test_images")
    return purl


def test_load_image_from_file(instruction):
    instruction.load_image.relative_file(__name__, "test_images/knit.svg")
    with open(KNIT_FILE) as knit_file:
        assert instruction.image == knit_file.read()


def test_choose_image_from_folder(knit):
    assert knit.raw_image == open(KNIT_FILE).read()


def test_purl_chose_right_image(purl):
    assert purl.raw_image == open(KNIT_FILE).read()



