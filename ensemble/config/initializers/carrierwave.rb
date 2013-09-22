CarrierWave.configure do |config|
  config.fog_credentials = {
    :provider               => 'AWS',                        # required
    :aws_access_key_id      => 'AKIAJU6AB5W4MKJFAC5A',                        # required
    :aws_secret_access_key  => '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',                        # required
  }
  config.fog_directory  = 'ensemble_bucket'                     # required
  config.fog_public     = true                                   # optional, defaults to true
  config.fog_attributes = {'Cache-Control'=>'max-age=315576000'}  # optional, defaults to {}
end
