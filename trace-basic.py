#from opentelemetry import trace

#tracer = trace.get_tracer(__name__)

#print(dir(trace))
#print(dir(tracer))

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("first-tracer")
print(tracer)

with tracer.start_as_current_span("first-span"):
   print("Hello, Welcome to tracing with OpenTelemetry!")