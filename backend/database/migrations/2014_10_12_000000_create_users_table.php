<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUsersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('username')->unique;
            $table->enum('type', ['admin', 'staff', 'student']);
            $table->datetime('last_login')->nullable();
            $table->datetime('last_logout')->nullable();
            $table->string('full_name')->nullable();
            $table->boolean('is_enabled')->default(true);
            $table->boolean('is_multilogin')->default(false);
            $table->string('description')->nullable();
            $table->string('password');
            $table->rememberToken();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('users');
    }
}
