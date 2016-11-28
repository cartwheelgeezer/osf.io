from framework.celery_tasks import app as celery_app
from scripts.analytics.base import DateAnalyticsHarness
from scripts.analytics.node_log_events import NodeLogEvents
from scripts.analytics.user_domain_events import UserDomainEvents


class EventAnalyticsHarness(DateAnalyticsHarness):

    @property
    def analytics_classes(self):
        return [NodeLogEvents, UserDomainEvents]


@celery_app.task(name='scripts.run_keen_events')
def run_main(date):
    EventAnalyticsHarness().main(date)


if __name__ == '__main__':
    EventAnalyticsHarness().main()
