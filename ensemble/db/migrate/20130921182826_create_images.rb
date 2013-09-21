class CreateImages < ActiveRecord::Migration
  def change
    create_table :images do |t|
      t.decimal :latitude
      t.decimal :longitude
      t.string :name
      t.datetime :capture_time
      t.string :model

      t.timestamps
    end
  end
end
