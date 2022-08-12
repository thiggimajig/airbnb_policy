from django.test import TestCase


# a separate TestClass for each model or view
# a separate test method for each set of conditions you want to test
# test method names that describe their function
# Django includes LiveServerTestCase to facilitate integration with tools like Selenium.
# Create your tests here.
#example here 
# class QuestionModelTests(TestCase):

#     def test_was_published_recently_with_future_question(self):
#         """
#         was_published_recently() returns False for questions whose pub_date
#         is in the future.
#         """
#         time = timezone.now() + datetime.timedelta(days=30)
#         future_question = Question(pub_date=time)
#         self.assertIs(future_question.was_published_recently(), False)
