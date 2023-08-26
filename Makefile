run:
	bundle exec jekyll serve --host 0.0.0.0 $@

install:
	gem install bundler && \
    bundle install
