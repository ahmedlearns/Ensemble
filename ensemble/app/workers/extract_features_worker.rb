class ExtractFeaturesWorker
  include Sidekiq::Worker

  def perform(id)
    puts "Doing hard work on #{Image.find(id).id}"

    uri = URI.parse("http://pygments.appspot.com/")
    request = Net::HTTP.post_form(uri)#, lang: @snippet.language, code: @snippet.plain_code)
#    @snippet.update_attribute(:highlighted_code, request.body)
    puts request
  end
end
