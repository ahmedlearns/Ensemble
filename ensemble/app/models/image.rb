class Image < ActiveRecord::Base
  attr_accessible :capture_time, :latitude, :longitude, :model, :name, :scrapboard_id, :group_id, :path

  belongs_to :scrapboard
  belongs_to :group

  mount_uploader :path, PhotoUploader

end
