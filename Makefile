run:
	bundle exec jekyll serve --host 0.0.0.0 $@

install:
	gem install bundler && \
    bundle install


packup:
	tar -zcf diary.tar.gz diary
	openssl enc -aes-256-cbc -salt -in diary.tar.gz -out diary.tar.gz.enc -pass pass:$(op read op://Personal/diary/password)
	rm diary.tar.gz
	rm -rf diary

unpack:
	openssl enc -aes-256-cbc -d -in diary.tar.gz.enc -out decrypted.tar.gz -pass pass:$(op read op://Personal/diary/password)
	tar xf decrypted.tar.gz --directory=.
	rm decrypted.tar.gz

