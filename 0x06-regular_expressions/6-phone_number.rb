#!/usr/bin/env ruby

# Check if the argument is provided
if ARGV.length != 1
    puts "Usage: #{$0} <phone_number>"
    exit 1
end

phone_number = ARGV[0].strip

# Check if the phone number matches the regular expression
if phone_number =~ /\A\d{10}\z/
    puts phone_number
else
    puts "Invalid phone number"
end
