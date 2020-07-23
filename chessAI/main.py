"""
Usage: chess train <schedule_file_path>

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt
from chessAI.model.training.campaign.factory import CampaignFactory


def main():

    arguments = docopt(__doc__)

    if arguments['train']:
        schedule_file_path = arguments['<schedule_file_path>']
        print('--- schedule file ---')
        with open(schedule_file_path) as f:
            print(f.read())
        print('---------------------')
        campaign = CampaignFactory.create_campaign_from_schedule_file(schedule_file_path)
        campaign.run()
