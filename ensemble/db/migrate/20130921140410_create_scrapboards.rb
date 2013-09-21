class CreateScrapboards < ActiveRecord::Migration
  def change
    create_table :scrapboards do |t|
      t.string :name

      t.timestamps
    end
  end
end
