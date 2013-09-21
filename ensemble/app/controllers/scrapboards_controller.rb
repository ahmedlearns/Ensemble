class ScrapboardsController < ApplicationController
  # GET /scrapboards
  # GET /scrapboards.json
  def index
    @scrapboards = Scrapboard.all

    respond_to do |format|
      format.html # index.html.erb
      format.json { render json: @scrapboards }
    end
  end

  # GET /scrapboards/1
  # GET /scrapboards/1.json
  def show
    @scrapboard = Scrapboard.find(params[:id])

    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @scrapboard }
    end
  end

  # GET /scrapboards/new
  # GET /scrapboards/new.json
  def new
    @scrapboard = Scrapboard.new

    respond_to do |format|
      format.html # new.html.erb
      format.json { render json: @scrapboard }
    end
  end

  # GET /scrapboards/1/edit
  def edit
    @scrapboard = Scrapboard.find(params[:id])
  end

  # POST /scrapboards
  # POST /scrapboards.json
  def create
    @scrapboard = Scrapboard.new(params[:scrapboard])

    respond_to do |format|
      if @scrapboard.save
        format.html { redirect_to @scrapboard, notice: 'Scrapboard was successfully created.' }
        format.json { render json: @scrapboard, status: :created, location: @scrapboard }
      else
        format.html { render action: "new" }
        format.json { render json: @scrapboard.errors, status: :unprocessable_entity }
      end
    end
  end

  # PUT /scrapboards/1
  # PUT /scrapboards/1.json
  def update
    @scrapboard = Scrapboard.find(params[:id])

    respond_to do |format|
      if @scrapboard.update_attributes(params[:scrapboard])
        format.html { redirect_to @scrapboard, notice: 'Scrapboard was successfully updated.' }
        format.json { head :no_content }
      else
        format.html { render action: "edit" }
        format.json { render json: @scrapboard.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /scrapboards/1
  # DELETE /scrapboards/1.json
  def destroy
    @scrapboard = Scrapboard.find(params[:id])
    @scrapboard.destroy

    respond_to do |format|
      format.html { redirect_to scrapboards_url }
      format.json { head :no_content }
    end
  end
end
