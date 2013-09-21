class AddGroupIdToImages < ActiveRecord::Migration
  def change
    add_column :images, :group_id, :integer
  end
end
