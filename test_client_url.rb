require 'socket'

port = 8888
host = "ec2-54-224-83-142.compute-1.amazonaws.com"

socket = TCPSocket.open(host,port)

  str = gets.chomp
  socket.puts(str)
    socket.close
  #puts line.chop      # And print with platform line terminator
