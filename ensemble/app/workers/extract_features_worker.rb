class ExtractFeaturesWorker
  include Sidekiq::Worker
  sidekiq_options retry: false


  def perform(id)
    image = Image.find(id)
    puts "Doing hard work on #{image.id}"

    port = 8888
    host = "ec2-54-224-83-142.compute-1.amazonaws.com"
    begin
      socket = TCPSocket.open(host,port)
      path = image.path
      string_to_send = {script: 0, url: path}
      socket.puts(string_to_send.to_json)
      puts string_to_send.to_json
      socket.close()
    rescue
      puts "Could not connect to server"

    end

    #uri = URI.parse("ec2-54-224-83-142.compute-1.amazonaws.com")
    #request = Net::HTTP.post_form(uri, lang: "aaa", code: "asas")


    #    @snippet.update_attribute(:highlighted_code, request.body)
  end
end
