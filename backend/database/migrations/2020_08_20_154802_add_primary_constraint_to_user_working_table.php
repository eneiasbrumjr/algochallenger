<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class AddPrimaryConstraintToUserWorkingTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::table('user_working', function (Blueprint $table) {
            $table->primary(['user_id', 'working_id'], 'user_working_primary');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::table('user_working', function (Blueprint $table) {
            $table->dropPrimary('user_working_primary');
        });
    }
}
