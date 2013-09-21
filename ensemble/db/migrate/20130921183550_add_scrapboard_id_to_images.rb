class AddScrapboardIdToImages < ActiveRecord::Migration
  def change
    add_column :images, :scrapboard_id, :integer
  end
end
