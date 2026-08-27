"""Rock, Paper, Scissors dataset."""

import re
import tensorflow_datasets.public_api as tfds

_TRAIN_URL = (
    "https://storage.googleapis.com/download.tensorflow.org/data/rps.zip"
)
_TEST_URL = "https://storage.googleapis.com/download.tensorflow.org/data/rps-test-set.zip"

_IMAGE_SIZE = 300
_IMAGE_SHAPE = (_IMAGE_SIZE, _IMAGE_SIZE, 3)

_NAME_RE = re.compile(
    r"^(rps|rps-test-set)(?:/|\\)(rock|paper|scissors)(?:/|\\)[\w-]*\.png$"
)


class Builder(tfds.core.GeneratorBasedBuilder):
  """Rock, Paper, Scissors dataset."""

  VERSION = tfds.core.Version("3.0.0")
  RELEASE_NOTES = {
      "3.0.0": "New split API (https://tensorflow.org/datasets/splits)",
  }

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(
                names=["rock", "paper", "scissors"]
            ),
        }),
        supervised_keys=("image", "label"),
        homepage="http://laurencemoroney.com/rock-paper-scissors-dataset",
    )

  def _split_generators(self, dl_manager):
    train_path, test_path = dl_manager.download([_TRAIN_URL, _TEST_URL])

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "archive": dl_manager.iter_archive(train_path),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "archive": dl_manager.iter_archive(test_path),
            },
        ),
    ]

  def _generate_examples(self, archive):
    """Generate rock, paper or scissors images and labels given the directory path.

    Args:
      archive: object that iterates over the zip.

    Yields:
      The image path and its corresponding label.
    """

    for fname, fobj in archive:
      res = _NAME_RE.match(fname)
      if not res:  # if anything other than .png; skip
        continue
      label = res.group(2).lower()
      record = {
          "image": fobj,
          "label": label,
      }
      yield fname, record