require 'test_helper'

class ScrapboardsControllerTest < ActionController::TestCase
  setup do
    @scrapboard = scrapboards(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:scrapboards)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create scrapboard" do
    assert_difference('Scrapboard.count') do
      post :create, scrapboard: { name: @scrapboard.name }
    end

    assert_redirected_to scrapboard_path(assigns(:scrapboard))
  end

  test "should show scrapboard" do
    get :show, id: @scrapboard
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @scrapboard
    assert_response :success
  end

  test "should update scrapboard" do
    put :update, id: @scrapboard, scrapboard: { name: @scrapboard.name }
    assert_redirected_to scrapboard_path(assigns(:scrapboard))
  end

  test "should destroy scrapboard" do
    assert_difference('Scrapboard.count', -1) do
      delete :destroy, id: @scrapboard
    end

    assert_redirected_to scrapboards_path
  end
end
