# This class will represent quiz objects that will be played in the game
from telegram import Poll, PollOption


def test_poll(update, context) -> Poll:
    sample_poll = Poll(
        id="1",
        question="What is the president of Cameroon?",
        options=[
            PollOption(text="Paul", voter_count=0),
            PollOption(text="Andrew", voter_count=0),
            PollOption(text="Obama", voter_count=0)
        ],
        is_closed=False,
        is_anonymous=True,
        type=Poll.QUIZ,
        allows_multiple_answers=True,
        correct_option_id=1,
        open_period=60,
        total_voter_count=20
    )

    return sample_poll
