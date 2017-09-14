import opentracing
import logging


def init_opentracing_tracer(tracer, log_level=logging.WARN):
    if tracer == 'instana':
        import instana.options as instanaOpts  # noqa
        import instana.tracer  # noqa

        instana.tracer.init(instanaOpts.Options(service='zmon-worker', log_level=log_level))
    elif tracer == 'basic':
        from basictracer import BasicTracer  # noqa

        opentracing.tracer = BasicTracer()

    else:
        opentracing.tracer = opentracing.Tracer()
