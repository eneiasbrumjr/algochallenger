<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateProblemsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('problems', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('working_id');
            $table->string('name');
            $table->string('full_name');
            $table->string('base_file_name');
            $table->string('description_file_name')->nullable();
            $table->timestamps();

            $table->foreign('working_id')->references('id')->on('workings');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('problems');
    }
}
