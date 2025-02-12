# https://stackoverflow.com/questions/27099427/jekyll-filename-without-date -->
 class Jekyll::PostReader
    # Don't use DATE_FILENAME_MATCHER so we don't need to put those stupid dates
    # in the filename. 
    def read_posts(dir)
      read_publishable(dir, "content", /.*\.md$/)
    end
  end