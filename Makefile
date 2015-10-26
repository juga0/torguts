


HTML= \
	00-overview.html \
	01-common-utils.html \
	02-dataflow.html

PNG = \
	diagrams/02/02-dataflow.png \
	diagrams/02/02-connection-types.png

all: generated

generated: $(HTML) $(PNG)

%.html: %.md
	maruku $< -o $@

%.png: %.dia
	dia $< --export=$@
