import yaml
from chessAI.model.training.campaign.random_walk import RandomWalkTrainingCampaign
from chessAI.util.error import MissingParameterError


class CampaignFactory:

    @staticmethod
    def create_campaign_from_schedule_file(schedule_file_path):

        with open(schedule_file_path) as f:
            schedule = yaml.safe_load(f.read())

        if 'class' not in schedule:
            raise MissingParameterError('class')

        campaign_class_name = schedule['class']

        if campaign_class_name == RandomWalkTrainingCampaign.__name__:
            rwtc = RandomWalkTrainingCampaign.from_schedule(schedule)
            return rwtc
